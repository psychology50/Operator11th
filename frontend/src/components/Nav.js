const Nav = (props) => {
    return (
      <nav>
        <ol>
          {props.topics.map((t) => (
            <li key={t.id}>
              <a
                id={t.id}
                href={'/read' + t.id}
                onClick={(e) => {
                  e.preventDefault();
                  props.onChangeMode(Number(e.target.id));
                }}
              >{t.title}</a>
            </li>
          ))}
        </ol>
      </nav>
    )
  }

export default Nav;