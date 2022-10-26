<script setup>
import { useAuthStore } from '@/stores';

const authStore = useAuthStore();
</script>

    <template>
        <nav v-show="authStore.user" class="navbar is-primary">
            <div class="navbar-menu">
                <div class="navbar-start">
                    <router-link to="/" class="navbar-item">Home</router-link>
                </div>
                
                <!-- <router-link to="/users" class="nav-item nav-link">Users</router-link>
                <button @click="authStore.logout()" class="btn btn-link nav-item nav-link">Logout</button> -->
            </div>

            <div class="navbar-end">
                <div class="navbar-item">
                    <button @click="authStore.logout()" class="button is-primary">Logout</button>
                </div>
            </div>
        </nav>
    </template>
