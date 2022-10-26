<script setup>
import { Form, Field } from 'vee-validate';
import * as Yup from 'yup';

import { useAuthStore } from '@/stores';

const schema = Yup.object().shape({
  username: Yup.string().required('Username is required'),
  password: Yup.string().required('Password is required'),
});

async function onSubmit(values) {
  const authStore = useAuthStore();
  const { username, password } = values;
  await authStore.login(username, password);
}
</script>

<template>
    <div class="column is-offset-one-quarter is-two-fifths">
        <div class="card">
            <div class="card-header is-justify-content-center py-4">
                <p class="title is-2">Вход</p>
            </div>
            <div class="card-body">
                <Form @submit="onSubmit" :validation-schema="schema" v-slot="{ errors, isSubmitting }">
                    <div class="column mx-3 form-group">
                        <label for="username">Имя пользователя</label>
                        <Field name="username" id="username" type="text" class="form-control input is-3" :class="{ 'is-danger': errors.username }" />
                        <div class="help is-danger">{{ errors.username }}</div>
                    </div>
                    <div class="column mx-3 form-group">
                        <label for="password">Пароль</label>
                        <Field name="password" id="password" type="password" class="form-control input is-1" :class="{ 'is-danger': errors.password }" />
                        <div class="help is-danger">{{ errors.password }}</div>
                    </div>
                    <div class="field is-grouped is-justify-content-center pb-4">
                        <p class="control">
                            <button type="submit" class="button is-link" :disabled="isSubmitting">
                            <span v-show="isSubmitting" class="is-loading"></span>
                                Вход
                            </button>
                        </p>
                        <p class="control is-one-fifth">
                            <router-link to="register" class="button is-link is-light">Регистрация</router-link>
                        </p>
                    </div>
                </Form>
            </div>
        </div>
    </div>
</template>
