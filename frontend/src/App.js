export default function App() {
  const user = {
    firstName: 'Yang',
    lastName: 'JaeSeo'
  }

  const formatName = (user) => {
    return user.firstName + ' ' + user.lastName;
  }

  return (
    <h1>Hello, {formatName(user)}!</h1>
  );
}
