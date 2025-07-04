import TodoPage from './Todo.svelte';
import BoardPage from './Board.svelte';

export default {
  '/todo': TodoPage,
  '/board': BoardPage,
  '*': TodoPage  // 기본은 투두
};