const Article = (props) => {
    return (
      <article id="article">
        <h2>{props.title}</h2>
        {props.body}
      </article>
    );
  }

export default Article;