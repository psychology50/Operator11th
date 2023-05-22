import {useState} from 'react'

function Update(props) {
    const [title, setTitle] = useState(props.title);
    const [body, setBody] = useState(props.body);

    const handleSubmit = (e) => {
        e.preventDefault();
        props.onUpdate(title, body);
    };

    return (
      <article id="input_form">
        <h2>Update</h2>
        <form onSubmit={handleSubmit}>
          <p><input type="text" name="title" placeholder="title" value={title} 
            onChange={(e)=>{setTitle(e.target.value); }}/></p>
          <p><textarea name="body" placeholder="body" value={body} 
            onChange={(e)=>{setBody(e.target.value);}}/></p>
          <p><input type="submit" value="Update"></input></p>
        </form>
      </article>
    );
  }

export default Update;