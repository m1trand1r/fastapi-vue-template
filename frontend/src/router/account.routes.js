import { LayoutView, LoginView, RegisterView } from '@/views/account';

export default {
  path: '/account',
  component: LayoutView,
  children: [
    { path: '', redirect: 'login' },
    { path: 'login', component: LoginView },
    { path: 'register', component: RegisterView },
  ],
};
