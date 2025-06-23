<script>
  import { onMount } from 'svelte';
  import { getTodos, addTodo } from './lib/api.js';

  let todos = [];
  let newTitle = '';

  onMount(async () => {
    todos = await getTodos();
  });

  async function handleAdd() {
    const todo = await addTodo(newTitle);
    todos = [...todos, todo];
    newTitle = '';
  }
</script>

<h1>할 일 목록</h1>

<input bind:value={newTitle} placeholder="할 일 입력" />
<button on:click={handleAdd}>추가</button>

<ul>
  {#each todos as todo}
    <li>{todo.title} {todo.completed ? '✅' : ''}</li>
  {/each}
</ul>
