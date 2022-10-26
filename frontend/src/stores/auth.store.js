import { defineStore } from 'pinia';

import { reqWrapper } from '@/helpers';
import { router } from '@/router';
import { useAlertStore } from '@/stores';

const baseUrl = `/login`;

export const useAuthStore = defineStore({
  id: 'auth',
  state: () => ({
    user: JSON.parse(localStorage.getItem('user')),
    returnUrl: null,
  }),
  actions: {
    async login(username, password) {
      try {
        const user = await reqWrapper.post(`${baseUrl}/authenticate`, { username, password });

        this.user = user;

        localStorage.setItem('user', JSON.stringify(user));

        router.push(this.returnUrl || '/users');
      } catch (error) {
        const alertStore = useAlertStore();
        alertStore.error(error);
      }
    },
    logout() {
      this.user = null;
      localStorage.removeItem('user');
      router.push('/account/login');
    },
  },
});
