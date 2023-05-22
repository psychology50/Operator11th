import React from 'react';
import {BrowserRouter, Route, Routes} from 'react-router-dom';
import {SignInPage, MainPage} from './pages';

import WrapperContainer from './styles/WrapperContainer.styled';

const App = () => {

  return(
    <BrowserRouter> 
      <WrapperContainer>
        <Routes>
          <Route path="/login" element={<SignInPage />}/>
          {/* <Route path="/register" element={<RegisterPage />}/> */}
          <Route path="/" element={<MainPage />} />
          {/* <Route path="/*" element={<NotFoundPage />}/> */} {/* 404 Not Found */}
        </Routes>
      </WrapperContainer>
    </BrowserRouter>
  );
}

export default App;
