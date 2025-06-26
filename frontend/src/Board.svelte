<script>
  import { onMount } from 'svelte';
  import { getPosts, createPost } from './lib/api.js';

  let posts = [];
  let title = '';
  let content = '';
  let author = '';
  let error = '';

  async function loadPosts() {
    try {
      const data = await getPosts();
      posts = Array.isArray(data) ? data : [];
    } catch (e) {
      error = '게시글을 불러오는 중 오류가 발생했습니다.';
      console.error('loadPosts error:', e);
      posts = [];
    }
  }

  async function handleCreatePost() {
    if (!title || !content || !author) {
      error = '모든 필드를 입력하세요.';
      return;
    }

    try {
      await createPost({ title, content, author });
      title = content = author = '';
      error = '';
      await loadPosts();
    } catch (e) {
      error = '게시글 작성 중 오류가 발생했습니다.';
      console.error('createPost error:', e);
    }
  }

  onMount(loadPosts);
</script>

<style>
  textarea {
    display: block;
    width: 100%;
    max-width: 500px;
    height: 100px;
    margin-bottom: 0.5rem;
    padding: 0.5rem;
    font-size: 1rem;
    border: 1px solid #ccc;
    border-radius: 4px;
  }
  .error {
    color: red;
    margin-bottom: 1rem;
  }
</style>

<h2>📌 게시판</h2>

<input placeholder="작성자" bind:value={author} />
<input placeholder="제목" bind:value={title} />
<textarea placeholder="내용" bind:value={content}></textarea>
<button on:click={handleCreatePost}>게시글 작성</button>

{#if error}
  <div class="error">{error}</div>
{/if}

<ul>
  {#each posts as post}
    <li>
      <strong>{post.title}</strong> by {post.author}<br />
      {post.content}
    </li>
  {/each}
</ul>
