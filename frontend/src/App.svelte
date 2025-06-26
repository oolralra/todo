<script>
  import { onMount } from 'svelte';
  import Board from './Board.svelte';

  let todos = [];
  let newTitle = '';

  let email = '';
  let password = '';
  let token = '';
  let error = '';

  async function handleLogin() {
    try {
      const res = await fetch('/api/login', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ username: email, password })
      });

      if (!res.ok) throw new Error('로그인 실패');

      const data = await res.json();
      token = data.username;  // 간단한 인증 방식: username을 토큰처럼 사용
      localStorage.setItem('token', token);
      error = '';
      await loadTodos();
    } catch (err) {
      error = err.message;
    }
  }

  async function loadTodos() {
    const storedToken = localStorage.getItem('token');
    if (!storedToken) return;
    token = storedToken;

    const res = await fetch('/api/todos/');
    todos = await res.json();
  }

  async function handleAdd() {
    if (!newTitle.trim()) return;

    const res = await fetch('/api/todos/', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ title: newTitle })
    });
    const todo = await res.json();
    todos = [...todos, todo];
    newTitle = '';
  }

  function handleLogout() {
    localStorage.removeItem('token');
    token = '';
    todos = [];
  }

  onMount(loadTodos);
</script>

<style>
  body {
    font-family: 'Segoe UI', sans-serif;
    background-color: #f9f9f9;
    margin: 0;
    padding: 2rem;
  }
  input {
    margin-bottom: 0.5rem;
    padding: 0.5rem;
    font-size: 1rem;
    width: 100%;
    max-width: 300px;
    border: 1px solid #ccc;
    border-radius: 4px;
  }
  button {
    margin-bottom: 1rem;
    padding: 0.5rem 1rem;
    margin-right: 0.5rem;
  }
  .error {
    color: red;
  }
</style>

{#if !token}
  <h1>로그인</h1>
  <input placeholder="Email" bind:value={email} />
  <input type="password" placeholder="Password" bind:value={password} />
  <button on:click={handleLogin}>로그인</button>
  {#if error}
    <div class="error">{error}</div>
  {/if}
{:else}
  <h2>Todo</h2>
  <button on:click={handleLogout}>로그아웃</button>
  <div class="todo-input">
    <input bind:value={newTitle} placeholder="새 할 일" />
    <button on:click={handleAdd}>추가</button>
  </div>
  <ul>
    {#each todos as todo}
      <li>{todo.title}</li>
    {/each}
  </ul>
  <!-- ✅ 게시판 삽입 -->
  <Board />
{/if}