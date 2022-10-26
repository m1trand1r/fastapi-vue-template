<script setup>
import { storeToRefs } from 'pinia';

import { useAlertStore } from '@/stores';

const alertStore = useAlertStore();
const { alert } = storeToRefs(alertStore);
</script>

    <template>
        <div v-if="alert" class="container">
            <div class="column is-offset-one-quarter is-two-fifths">
                <div class="notification" :class="alert.type">
                    <button @click="alertStore.clear()" class="delete">&times;</button>
                    {{alert.message}}
                </div>
            </div>
        </div>
    </template>
