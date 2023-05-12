import {useState} from 'react';
import {Header, Nav, Article, Create, Update} from "./components";

function App() {
  const [mode, setMode] = useState('WELCOME');
  const [id, setId] = useState(null);
  const [nextId, setNextId] = useState(4);

  const [topics, setTopics] = useState([
    {id: 1, title: 'html', body: 'html is ...'},
    {id: 2, title: 'css', body: 'css is ...'},
    {id: 3, title: 'js', body: 'javascript is ...'},
  ])

  // 선언형 프로그래밍으로 수정된 부분 시작
  const handleModeChange = (newMode) => {
    setMode(newMode);
  };

  const handleTopicClick = (topicId) => {
    setMode('READ');
    setId(topicId);
  };

  const handleCreate = (_title, _body) => {
    const newTopic = { id: nextId, title: _title, body: _body };
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

  if (mode === 'WELCOME') {
    content = <Article title="Welcome" body="Hello, WEB"/>
  } else if (mode === 'READ') {
    const topic = topics.find(topic => topic.id === id);

    content = <Article title={topic.title} body={topic.body}/>
    contextControl= <li><a href={'/update/' + id} onClick={(e)=>{
      e.preventDefault();
      setMode('UPDATE');  
    }}>Update</a></li> 
  } else if (mode === 'CREATE') {
    content = <Create onCreate={handleCreate} />;
  } else if (mode === 'UPDATE') {
    const topic = topics.find((topic) => topic.id === id);
    content = <Update
      title={topic.title}
      body={topic.body}
      onUpdate={handleUpdate}
    />
  }
  
  return (
    <div>
      <Header 
        title="React" onChangeMode={() => {
          handleModeChange('WELCOME');
        }}
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
