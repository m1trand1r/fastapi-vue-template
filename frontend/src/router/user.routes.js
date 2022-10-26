import { LayoutUser, ListUsers } from '@/views/users';

export default {
  path: '/users',
  component: LayoutUser,
  children: [
    { path: '', component: ListUsers },
    // { path: 'add', component: AddEdit },
    // { path: 'edit/:id', component: AddEdit },
  ],
};
