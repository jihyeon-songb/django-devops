<template>
  <div>
    <h1>TodoList</h1>
    <input v-model="newTodo" type="text" @keypress.enter="createTodo">
    <button @click="createTodo">확인</button>
    <div v-for="(todo, idx) in todoList" :key="idx">
      <!-- 수정중이 아닐 때 -->
      <div v-if="true">
        <span @click="updateLine(todo.id)" :class="{ line:todo.line }">{{todo.text}}</span>
        <button @click="updateTodo(todo.id)">✏️</button>
        <button @click="deleteTodo(todo.id)">❌</button>
      </div>
      <!--  수정중 일 때   -->
<!--      <div v-else>-->
<!--        <input type="text" v-model="todo.text" @keypress.enter="updateTodo(todo.id)">-->
<!--        <button @click="updateTodo(todo.id)">완료</button>-->
<!--      </div>-->
    </div>
  </div>
</template>

<script>
import axios from 'axios'

let url = 'https://jihyeon.pythonanywhere.com/api/todo/'

export default {
  name: "TodoLIst",
  data() {
    return {
      todoList: [],
      newTodo: '',
    }
  },
  created() {
    // 로컬스토리지에 저장된 투두 리스트가 있다면 불러온다
    this.getTodoList()
  },
  methods: {
    async getTodoList() {
      const response = await axios.get(url)
      this.todoList = response.data
    },
    async postTodo(todo) {
      const response = await axios.post(url,todo)
      console.log(response)
    },
    async createTodo() {
      const todo = {
        // 나의 투두
        text: this.newTodo,
        // 투두의 id
        // 투두를 완료했으면 true가 되고 줄이 그어진다.
        line: false,
        // update하고 있는 투두인지.
      }
      this.postTodo(todo)
      this.newTodo = ''
    },
    deleteTodo(id) {
      // delete할 투두 삭제
      this.todoList = this.todoList.filter((todo) => todo.id !== parseInt(id))
      this.saveTodoList()
    },
    updateTodo(id){
      const updateItem = this.todoList.filter((todo) => todo.id === parseInt(id))
      // update 중이 아니면 update, update 중이면 update 완료
      updateItem[0].update =!updateItem[0].update
      this.saveTodoList()
    },
    updateLine(id){
      const lineItem = this.todoList.filter((todo) => todo.id === parseInt(id))
      // 줄 그어져있으면 없애고 줄 없으면 그어짐
      lineItem[0].line = !lineItem[0].line
      this.saveTodoList()
    }
  }
}
</script>

<style scoped>
.line{
  text-decoration: line-through;
}
</style>