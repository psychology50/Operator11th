import {useState} from 'react';

function Create(props) {
  const [title, setTitle] = useState('');
  const [body, setBody] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    props.onCreate(title, body);
  };

    return (
      <article>
        <h2>Create</h2>
        <form onSubmit={handleSubmit}>
          <p><input type="text" name="title" placeholder="title" 
                onChange={(e) => setTitle(e.target.value)}/></p>
          <p><textarea name="body" placeholder="body" value={body}
                onChange={(e) => setBody(e.target.value)}/></p>
          <p><input type="submit" value="Creat"></input></p>
        </form>
      </article>
    );
  }

export default Create;