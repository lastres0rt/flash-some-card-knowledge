import React, { Component } from "react";
import {
  Button,
  ButtonGroup,
  Form,
  FormGroup,
//  Input,
//  Label,
} from "reactstrap";
// import Modal from "./components/Modal";
import axios from "axios";

axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = 'X-CSRFToken'

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      viewCompleted: false,
      flashcardList: [],
      modal: false,
      activeItem: {
        question: "",
        choices: ["", "", "", ""],
      },
    };
  }

  componentDidMount() {
    this.refreshList();
  }

  refreshList = () => {
    axios
      .get("/random_question")
      // .get("/api/flashcards")
      .then((res) => this.setState({ flashcardList: [res.data] }))
      .catch((err) => console.log(err));
  };

  toggle = () => {
    this.setState({ modal: !this.state.modal });
  };

  handleSubmit = (item) => {
    this.toggle();

    if (item.id) {
      axios
        .put(`/api/flashcards/${item.id}/`, item)
        .then((res) => this.refreshList());
      return;
    }
    axios
      .post("/api/flashcards/", item)
      .then((res) => this.refreshList());
  };

  handleDelete = (item) => {
    axios
      .delete(`/api/flashcards/${item.id}/`)
      .then((res) => this.refreshList());
  };

  createItem = () => {
    const item = { title: "", description: "", completed: false };

    this.setState({ activeItem: item, modal: !this.state.modal });
  };

  editItem = (item) => {
    this.setState({ activeItem: item, modal: !this.state.modal });
  };

  displayCompleted = (status) => {
    if (status) {
      return this.setState({ viewCompleted: true });
    }

    return this.setState({ viewCompleted: false });
  };
  
  submitAnswer = (item) => {
    axios
      .post(`/api/choices/${item.id}/`, item)
      .then((res) => this.refreshList());
  };

 renderTabList = () => {
    return (
      <div className="nav nav-tabs">
        <span
          className={this.state.viewCompleted ? "nav-link active" : "nav-link"}
          onClick={() => this.displayCompleted(true)}
        >
          1
        </span>
        <span
          className={this.state.viewCompleted ? "nav-link" : "nav-link active"}
          onClick={() => this.displayCompleted(false)}
        >
          2
        </span>
        <span
          className={this.state.viewCompleted ? "nav-link" : "nav-link active"}
          onClick={() => this.displayCompleted(false)}
        >
          2
        </span>
      </div>
    );
  };

  renderItems = () => {
    // const { viewCompleted } = this.state;
    // const newItems = this.state.flashcardList.filter(
    //   (item) => item.completed === viewCompleted
    // ); 

    return this.state.flashcardList.map((item) => (
      <li
        key={item.id}
        className="list-group-item d-flex justify-content-between align-items-center"
      >
        <span
          className={'flashcard-title mr-2'}
          title={item.question}
        >
          {item.question}
        </span>
        <span>
          <Form>
            <FormGroup>
              <ButtonGroup vertical>
                {item.choices.map((choice) =>(
                  /* <Button onClick={() => this.submitAnswer(choice)}>{choice.choice_text}</Button> */
                  <Button>{choice.choice_text}</Button>
                ))}
                {/* <Button>{item.choices[0].choice_text}</Button>
                <Button>{item.choices[1].choice_text}</Button>
                <Button>{item.choices[2].choice_text}</Button>
                <Button>{item.choices[3].choice_text}</Button> */}
              </ButtonGroup>
            </FormGroup>
          </Form>
        </span>
        {/* <span>
          <button
            className="btn btn-secondary mr-2"
            onClick={() => this.editItem(item)}
          >
            Answer
          </button>
        </span> */}
      </li>
    ));
  };

  render() {
    return (
      <main className="container">
        <h1 className="text-white text-uppercase text-center my-4">3D Printing Flashcards</h1>
        <div className="row">
          <div className="col-md-6 col-sm-10 mx-auto p-0">
            <div className="card p-3">
              {/* <div className="mb-4">
                <button
                  className="btn btn-primary"
                  onClick={this.createItem}
                >
                  Add task
                </button>
              </div> */}
              {/* {this.renderTabList()} */}
              <ul className="list-group list-group-flush border-top-0">
                {this.renderItems()}
              </ul>
            </div>
          </div>
        </div>
        {this.state.modal ? (
          <Modal
            activeItem={this.state.activeItem}
            toggle={this.toggle}
            onSave={this.handleSubmit}
          />
        ) : null}
      </main>
    );
  }
}

export default App;