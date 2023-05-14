import {useState} from 'react';
import {Header, Nav, Article, Create, Update} from "./components";

const App = () => {
  const [mode, setMode] = useState('WELCOME');
  const [id, setId] = useState(null);
  const [nextId, setNextId] = useState(4);

  const [topics, setTopics] = useState([
    {id: 1, title: 'html', body: 'html is ...'},
    {id: 2, title: 'css', body: 'css is ...'},
    {id: 3, title: 'js', body: 'javascript is ...'},
  ])

  const handleTopicClick = (topicId) => {
    setMode('READ');
    setId(topicId);
  };

  const handleCreate = (title, body) => {
    const newTopic = { id: nextId, title: title, body: body };
    const newTopics = [...topics, newTopic];

    setTopics(newTopics);
    setMode('READ');
    setId(nextId);
    setNextId(nextId + 1);
  };

  const handleUpdate = (title, body) => {
    const newTopics = topics.map((topic) =>
      topic.id === id ? { ...topic, title: title, body: body } : topic
    );

    setTopics(newTopics);
    setMode('READ');
  };

  let content = null;
  let contextControl = null; 
  let topic = null;

  switch (mode) {
    case 'WELCOME':
      content = <Article title="Welcome" body="Hello, WEB"/>;
      break;
    case 'READ':
      topic = topics.find((topic) => topic.id === id);
      content = <Article title={topic.title} body={topic.body}/>;
      contextControl = <li>
          <a href={'/update/' + id} onClick={(e)=>{
              e.preventDefault();
              setMode('UPDATE');  
            }
          }> Update </a>
        </li>
      break;
    case 'CREATE':
      content = <Create onCreate={handleCreate} />;
      break;
    case 'UPDATE':
      topic = topics.find((topic) => topic.id === id);
      content = <Update title={topic.title} body={topic.body} onUpdate={handleUpdate}/>
      break;
    default: break;
  }

  return (
    <div>
      <Header 
        title="React" 
        onChangeMode={() => {setMode('WELCOME');}}
      />
      <Nav 
        topics={topics} 
        onChangeMode={handleTopicClick}
      />

      {content}

      <ul>
        <li>
          <a href="/create" onClick={(e)=>{
            e.preventDefault();
            setMode('CREATE');
          }}>Create</a>
        </li>
        {contextControl}
      </ul>
    </div>

  );
}

export default App;
