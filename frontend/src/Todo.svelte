<!-- frontend/src/Todo.svelte -->
<script>
  import { onMount } from 'svelte';

  let todos = [];
  let newTitle = '';
  let error = '';

  async function loadTodos() {
    try {
      const res = await fetch('/api/todos/');
      todos = await res.json();
    } catch (e) {
      error = '할 일을 불러오는 중 오류가 발생했습니다.';
      console.error(e);
    }
  }

  async function handleAddTodo() {
    if (!newTitle.trim()) {
      error = '할 일을 입력하세요';
      return;
    }
    try {
      const res = await fetch('/api/todos/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ title: newTitle })
      });
      if (!res.ok) throw new Error('추가 실패');
      const todo = await res.json();
      todos = [...todos, todo];
      newTitle = '';
      error = '';
    } catch (e) {
      error = '할 일 추가 중 오류가 발생했습니다.';
      console.error(e);
    }
  }

  onMount(loadTodos);
</script>

<h2>✅ 투두 리스트</h2>
<input placeholder="할 일 입력" bind:value={newTitle} />
<button on:click={handleAddTodo}>추가</button>
{#if error}<div class="error">{error}</div>{/if}
<ul>
  {#each todos as todo}
    <li>{todo.title}</li>
  {/each}
</ul>