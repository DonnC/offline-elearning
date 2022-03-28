<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <h1>
          Books
        </h1>
        <hr><br><br>
        <button
          v-b-modal.book-modal
          type="button"
          class="btn btn-success btn-sm"
        >
          Add Book
        </button>
        <br><br>
        <table class="table table-hover">
          <thead>
            <tr>
              <th scope="col">
                Title
              </th>
              <th scope="col">
                Author
              </th>
              <th scope="col">
                Read?
              </th>
            </tr>
          </thead>
          <tbody>
            <tr
              v-for="(book, index) in books"
              :key="index"
            >
              <td>
                {{ book.title }}
              </td>
              <td>
                {{ book.author }}
              </td>
              <td>
                <span v-if="book.read"> Yes

                </span>
                <span v-else>No</span>
              </td>
              <td>
                <div
                  class="btn-group"
                  role="group"
                >
                  <button
                    type="button"
                    class="btn btn-warning btn-sm"
                  >
                    Update
                  </button>
                  <button
                    type="button"
                    class="btn btn-danger btn-sm"
                  >
                    Delete
                  </button>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>

    <b-modal
      id="book-modal"
      ref="addBookModal"
      title="Add a new book"
      hide-footer
    >
      <b-form
        class="w-100"
        @submit="onSubmit"
        @reset="onReset"
      >
        <b-form-group
          id="form-title-group"
          label="Title:"
          label-for="form-title-input"
        >
          <b-form-input
            id="form-title-input"
            v-model="addBookForm.title"
            type="text"
            required
            placeholder="Enter title"
          />
        </b-form-group>

        <b-form-group
          id="form-author-group"
          label="Author:"
          label-for="form-author-input"
        >
          <b-form-input
            id="form-author-input"
            v-model="addBookForm.author"
            type="text"
            required
            placeholder="Enter author"
          />
        </b-form-group>

        <b-form-group
          id="form-read-group"
        >
          <b-form-checkbox-group
            id="form-checks"
            v-model="addBookForm.read"
          > 
            <b-form-checkbox value="true">
              Read?
            </b-form-checkbox>
          </b-form-checkbox-group>
        </b-form-group>

        <b-button-group>
          <b-button
            type="submit"
            variant="primary"
          >
            Submit
          </b-button>
          <b-button
            type="reset"
            variant="danger"
          >
            Reset
          </b-button>
        </b-button-group>
      </b-form>
    </b-modal>
  </div>
</template>

<script>
import axios from 'axios';
import { baseUrl } from '../constants/constants.js';

export default {
  data() {
    return {
      books: [],
      addBookForm: {
        title: '',
        author: '',
        read: []
      }
    };
  },

  created() {
    this.getBooks();
  },

  methods: {
    initForm() {
      this.addBookForm.read = [],
      this.addBookForm.title = '',
      this.addBookForm.author = '';
    },
    getBooks() {
      const path = baseUrl;

      axios.get(path)
        .then((res) => {
          this.books = res.data.books;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    addBook(payload) {
      const path = baseUrl;

      axios.post(path, payload)
        .then(() => {
          this.getBooks();
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    onSubmit(evt) {
      // prevent the normal browser behavior
      evt.preventDefault();

      this.$refs.addBookModal.hide();

      let read = false;

      if(this.addBookForm.read[0]) read = true;

      const payload = {
        title: this.addBookForm.title,
        author: this.addBookForm.author,
        read
      };

      this.addBook(payload);

      this.initForm();
    },
    onReset(evt) {
      evt.preventDefault();

      this.$refs.addBookModal.hide();
      this.initForm();
    }
  }
};
</script>
