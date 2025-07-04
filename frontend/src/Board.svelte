<!-- frontend/src/Board.svelte -->
<script>
  import { onMount } from 'svelte';

  let posts = [];
  let title = '';
  let content = '';
  let author = '';
  let error = '';

  async function loadPosts() {
    try {
      const res = await fetch('/api/posts/');
      posts = await res.json();
    } catch (e) {
      error = '게시글을 불러오는 중 오류가 발생했습니다.';
      console.error(e);
    }
  }

  async function handleCreatePost() {
    if (!title || !content || !author) {
      error = '모든 필드를 입력하세요.';
      return;
    }
    try {
      const res = await fetch('/api/posts/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ title, content, author })
      });
      if (!res.ok) throw new Error('작성 실패');
      title = content = author = '';
      error = '';
      await loadPosts();
    } catch (e) {
      error = '게시글 작성 중 오류가 발생했습니다.';
      console.error(e);
    }
  }

  onMount(loadPosts);
</script>

<h2>📌 게시판</h2>
<input placeholder="작성자" bind:value={author} />
<input placeholder="제목" bind:value={title} />
<textarea placeholder="내용" bind:value={content}></textarea>
<button on:click={handleCreatePost}>게시글 작성</button>
{#if error}<div class="error">{error}</div>{/if}
<ul>
  {#each posts as post}
    <li><strong>{post.title}</strong> by {post.author}<br />{post.content}</li>
  {/each}
</ul>
