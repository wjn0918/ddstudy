---
title: Logto
---

:::tabs

@tab react

https://cloud.logto.io/2hlv5n/applications/xskz9nsflxg1ont42aych/settings



App.jsx
```
import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'

import { LogtoProvider } from '@logto/react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Callback from './pages/Callback';
import { Home } from './pages/Home';


const config = {
  endpoint: 'https://2hlv5n.logto.app/',
  appId: 'xxx',
};


function App() {
  const [count, setCount] = useState(0)

  return (
    <>
     <BrowserRouter>
      <LogtoProvider config={config}>
        <Routes>
          <Route path="/worktime/" element={<Home />} />
          <Route path="/worktime/callback" element={<Callback />} />
        </Routes>
      </LogtoProvider>
    </BrowserRouter>
    </>
  )
}

export default App

```

Home/index.jsx

```
import { useLogto } from '@logto/react';

export const Home = () => {
  const { signIn, signOut, isAuthenticated } = useLogto();

  return isAuthenticated ? (
    <button onClick={() => signOut('http://localhost:5173/worktime')}>Sign Out</button>
  ) : (
    <button onClick={() => signIn('http://localhost:5173/worktime/callback')}>Sign In</button>
  );
};
```

Callback/index.jsx
```
import { useHandleSignInCallback } from '@logto/react';
import { useNavigate } from 'react-router-dom';

const Callback = () => {
  const navigate = useNavigate();
  const { isLoading } = useHandleSignInCallback(() => {
    navigate('/worktime');
  });

  return isLoading ? <p>Redirecting...</p> : null;
};

export default Callback;
```

:::