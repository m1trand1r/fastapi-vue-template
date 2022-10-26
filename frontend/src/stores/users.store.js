import { defineStore } from 'pinia';

import { reqWrapper } from '@/helpers';
import { useAuthStore } from '@/stores';
// import { api } from '@/api';

const baseUrl = `/users`;

// function postRequest() {
//   return (url, body) => {
//     console.log(`func ${url}, ${body}`);
//     return api.post(`${url}/register`, new URLSearchParams(body));
//   };
// }

export const useUsersStore = defineStore({
  id: 'users',
  state: () => ({
    users: {},
    user: {},
  }),
  actions: {
    async register(user) {
      await reqWrapper.post(`/register`, user);
    },
    async getAll() {
      this.users = { loading: true };
      try {
        this.users = await reqWrapper.get(baseUrl + "/all");
      } catch (error) {
        this.users = { error };
      }
    },
    async isAdmin() {
      return await reqWrapper.getAdmin(baseUrl + '/is_admin');
    },
    async getById(id) {
      this.user = { loading: true };
      try {
        this.user = await reqWrapper.get(`${baseUrl}/${id}`);
      } catch (error) {
        this.user = { error };
      }
    },
    async update(id, params) {
      await reqWrapper.put(`${baseUrl}/${id}`, params);

      // update stored user if the logged in user updated their own record
      const authStore = useAuthStore();
      if (id === authStore.user.id) {
        // update local storage
        const user = { ...authStore.user, ...params };
        localStorage.setItem('user', JSON.stringify(user));

        // update auth user in pinia state
        authStore.user = user;
      }
    },
    async delete(id) {
      // add isDeleting prop to user being deleted
      this.users.find((x) => x.id === id).isDeleting = true;

      await reqWrapper.delete(`${baseUrl}/${id}`);

      // remove user from list after deleted
      this.users = this.users.filter((x) => x.id !== id);

      // auto logout if the logged in user deleted their own record
      const authStore = useAuthStore();
      if (id === authStore.user.id) {
        authStore.logout();
      }
    },
  },
});
