import React from 'react';
import {createRoot} from 'react-dom/client';
import App from './App';
import {WordLookupProvider} from './WordLookup';
import './style.css';
createRoot(document.getElementById('root')!).render(<React.StrictMode><WordLookupProvider><App/></WordLookupProvider></React.StrictMode>);
