<script>
  import Router from 'svelte-spa-router';
  import routes from './routes';
</script>

<nav>
  <a href="#/todo">Todo</a>
  <a href="#/board">Board</a>
</nav>

<Router {routes} />
