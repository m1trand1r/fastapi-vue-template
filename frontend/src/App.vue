<script setup>
import { NavComp, AlertComp } from '@/components';
import { useAuthStore } from '@/stores';

const authStore = useAuthStore();
</script>

  <template>
      <div class="app-container" :class="authStore.user && 'bg-light'">
          <NavComp />
          <AlertComp />
          <div class="container pt-4 pb-4">
              <router-view />
          </div>
      </div>
  </template>

  <style>
  @import '@/assets/base.css';
  @import 'bulma/css/bulma.css';
  </style>
