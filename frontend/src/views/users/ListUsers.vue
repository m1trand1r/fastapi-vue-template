<script setup>
import { storeToRefs } from 'pinia';

import { useUsersStore } from '@/stores';

const usersStore = useUsersStore();
const { users } = storeToRefs(usersStore);
const is_admin = usersStore.isAdmin();
usersStore.getAll();
</script>

    <template>
        <h1>Users</h1>
        <!-- <router-link to="/users/add" class="btn btn-sm btn-success mb-2">Add User</router-link> -->
        <button :v-if="is_admin" class="button is-primary">тестовая кнопка</button>
        <div :v-show="is_admin">
            <table class="table">
            <thead>
                <tr>
                    <th style="width: 10%">ID</th>
                    <th style="width: 30%">Username</th>
                    <th style="width: 40%">Password hash</th>
                    <th style="width: 10%">is_active</th>
                    <th style="width: 10%">is_admin</th>
                </tr>
            </thead>
            <tbody>
                <template v-if="users.length">
                    <tr v-for="user in users" :key="user.id">
                        <h1 v-if="user.is_active">TEST TSES</h1>
                        <h1 v-if="user.is_superuser">TEST TSES</h1>
                        <td>{{ user.id }}</td>
                        <td>{{ user.username }}</td>
                        <td>{{ user.password }}</td>
                        <td>{{ user.is_active }}</td>
                        <td>{{ user.is_superuser }}</td>
                        <!-- <td style="white-space: nowrap">
                            <router-link :to="`/users/edit/${user.id}`" class="btn btn-sm btn-primary mr-1">Edit</router-link>
                            <button @click="usersStore.delete(user.id)" class="btn btn-sm btn-danger btn-delete-user" :disabled="user.isDeleting">
                                <span v-if="user.isDeleting" class="spinner-border spinner-border-sm"></span>
                                <span v-else>Delete</span>
                            </button>
                        </td> -->
                    </tr>
                </template>
                <!-- <tr v-if="users.loading">
                    <td colspan="4" class="text-center">
                        <span class="spinner-border spinner-border-lg align-center"></span>
                    </td>
                </tr> -->
                <tr v-if="users.error">
                    <td colspan="4">
                        <div class="text-danger">Error loading users: {{users.error}}</div>
                    </td>
                </tr>
            </tbody>
        </table>
        </div>
        
    </template>
