<template>
  <div>
    <h1>TodoList</h1>
    <input v-model="newTodo" type="text" @keypress.enter="createTodo">
    <button @click="createTodo">확인</button>
    <div v-for="(todo, idx) in todoList" :key="idx">
      <todo-item :todo="todo" :idx="idx" :todoList="todoList"></todo-item>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import TodoItem from "@/components/TodoItem";
// 배포 서버 url
let url = 'https://jihyeon.pythonanywhere.com/api/todo/'

export default {
  name: "TodoLIst",
  components: {
    TodoItem,
  },
  data() {
    return {
      todoList: [],
      newTodo: '',
    }
  },
  created() {
    // 투두 리스트 데이터 가져오기
    this.getTodoList()
  },
  methods: {
    // 투두 리스트 데이터 가져오기
    async getTodoList() {
      const response = await axios.get(url)
      this.todoList = response.data
    },
    // 투두 CREATE
    async postTodo(todo) {
      await axios.post(url,todo)
      .then((res) => {
        console.log(res)
        // 일단 푸시하고
        this.todoList.push(todo)
        // 다시 투두리스트 가져오기
        this.getTodoList()
      })
      .catch((err) => {
        console.log(err)
      })
    },
    createTodo() {
      const todo = {
        text: this.newTodo,
        line: false,
      }
      this.postTodo(todo)
      this.newTodo = ''
    },
  }
}
</script>

<style>
.line{
  text-decoration: line-through;
}
</style>