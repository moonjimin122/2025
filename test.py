/*
Updated React + Vite + Tailwind Travel Recommender
Now includes 20 places (5 for each theme: city, nature, culture, history)
*/

// package.json
{
  "name": "travel-recommender-app",
  "version": "0.1.0",
  "private": true,
  "scripts": {
    "dev": "vite",
    "build": "vite build",
    "preview": "vite preview"
  },
  "dependencies": {
    "react": "^18.2.0",
    "react-dom": "^18.2.0"
  },
  "devDependencies": {
    "vite": "^5.0.0",
    "@vitejs/plugin-react": "^4.0.0",
    "tailwindcss": "^3.5.0",
    "postcss": "^8.4.21",
    "autoprefixer": "^10.4.14"
  }
}

// vite.config.js
import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
export default defineConfig({ plugins: [react()] })

// index.html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Travel Recommender</title>
  </head>
  <body>
    <div id="root"></div>
    <script type="module" src="/src/main.jsx"></script>
  </body>
</html>

// src/main.jsx
import React from 'react'
import { createRoot } from 'react-dom/client'
import App from './App'
import './index.css'
createRoot(document.getElementById('root')).render(<App />)

// src/data.js
export const PLACES = [
  // City
  { id:1, name:"Central Park, New York, USA", theme:"city", description:"Urban park in Manhattan", img:"https://images.unsplash.com/photo-1549921296-3b4b3b7f0d5c" },
  { id:2, name:"Shibuya Crossing, Tokyo, Japan", theme:"city", description:"World’s busiest pedestrian crossing", img:"https://images.unsplash.com/photo-1554797589-7241bb691973" },
  { id:3, name:"Marina Bay Sands, Singapore", theme:"city", description:"Iconic skyline and rooftop views", img:"https://images.unsplash.com/photo-1506377247377-2a5b3b417ebb" },
  { id:4, name:"Times Square, New York, USA", theme:"city", description:"Neon lights and entertainment hub", img:"https://images.unsplash.com/photo-1534447677768-be436bb09401" },
  { id:5, name:"Downtown Dubai, UAE", theme:"city", description:"Modern skyline with Burj Khalifa", img:"https://images.unsplash.com/photo-1506976785307-8732e854ad03" },

  // Nature
  { id:6, name:"Gullfoss, Iceland", theme:"nature", description:"Spectacular waterfall in Iceland", img:"https://images.unsplash.com/photo-1517821099604-0d55b2d01a6b" },
  { id:7, name:"Torres del Paine, Chile", theme:"nature", description:"Mountains and glaciers in Patagonia", img:"https://images.unsplash.com/photo-1508261306964-5a0b3b6e6d6b" },
  { id:8, name:"Grand Canyon, USA", theme:"nature", description:"World-famous canyon with breathtaking views", img:"https://images.unsplash.com/photo-1508264165352-258859e62245" },
  { id:9, name:"Mount Everest Base Camp, Nepal", theme:"nature", description:"Himalayan trekking destination", img:"https://images.unsplash.com/photo-1524492449090-1a065f3a1b48" },
  { id:10, name:"Great Barrier Reef, Australia", theme:"nature", description:"Largest coral reef system in the world", img:"https://images.unsplash.com/photo-1507525428034-b723cf961d3e" },

  // Culture
  { id:11, name:"Fushimi Inari, Kyoto, Japan", theme:"culture", description:"Torii gates and serene forested paths", img:"https://images.unsplash.com/photo-1549692520-acc6669e2f0c" },
  { id:12, name:"Angkor Wat, Cambodia", theme:"culture", description:"Largest temple complex in the world", img:"https://images.unsplash.com/photo-1504595403659-9088ce801e29" },
  { id:13, name:"Taj Mahal, India", theme:"culture", description:"Mughal Empire’s masterpiece mausoleum", img:"https://images.unsplash.com/photo-1548013146-72479768bada" },
  { id:14, name:"Sagrada Familia, Barcelona, Spain", theme:"culture", description:"Gaudí’s unfinished basilica", img:"https://images.unsplash.com/photo-1501594907352-04cda38ebc29" },
  { id:15, name:"Marrakech Medina, Morocco", theme:"culture", description:"Traditional markets and Islamic culture", img:"https://images.unsplash.com/photo-1524492449090-1a065f3a1b48" },

  // History
  { id:16, name:"Colosseum, Rome, Italy", theme:"history", description:"Ancient amphitheater in Italy", img:"https://images.unsplash.com/photo-1549893079-1f4f0f5b3df1" },
  { id:17, name:"Machu Picchu, Peru", theme:"history", description:"Incan citadel in the Andes", img:"https://images.unsplash.com/photo-1509112756314-34a0badb29d4" },
  { id:18, name:"Great Wall of China, China", theme:"history", description:"World’s longest defensive wall", img:"https://images.unsplash.com/photo-1524492449090-1a065f3a1b48" },
  { id:19, name:"Petra, Jordan", theme:"history", description:"Ancient rock-carved city", img:"https://images.unsplash.com/photo-1544986581-efac024faf62" },
  { id:20, name:"Pyramids of Giza, Egypt", theme:"history", description:"Symbol of ancient Egyptian civilization", img:"https://images.unsplash.com/photo-1534531688091-a45825799277" }
]

// src/App.jsx
import React, { useState, useMemo, useEffect } from 'react'
import { PLACES } from './data'

const THEMES = ['all','city','nature','culture','history']

export default function App() {
  const [theme, setTheme] = useState('all')
  const [query, setQuery] = useState('')
  const [favorites, setFavorites] = useState(() => {
    try { return JSON.parse(localStorage.getItem('fav_places')||'[]') } catch { return [] }
  })

  useEffect(()=>{ localStorage.setItem('fav_places', JSON.stringify(favorites)) },[favorites])

  const filtered = useMemo(()=>{
    return PLACES.filter(p => (theme==='all'||p.theme===theme) && (p.name.toLowerCase().includes(query.toLowerCase())||p.description.toLowerCase().includes(query.toLowerCase())))
  },[theme,query])

  const toggleFav = (id)=> setFavorites(prev => prev.includes(id)? prev.filter(x=>x!==id) : [...prev,id])

  const randomPick = ()=>{
    if(filtered.length===0) return alert("조건에 맞는 장소가 없습니다.")
    const p = filtered[Math.floor(Math.random()*filtered.length)]
    alert(`${p.name}: ${p.description}`)
  }

  return (
    <div className="min-h-screen bg-slate-50 p-6">
      <h1 className="text-2xl font-bold mb-4">세계 여행지 추천</h1>
      <div className="mb-4 flex gap-2 flex-wrap">
        {THEMES.map(t=>(
          <button key={t} onClick={()=>setTheme(t)} className={`px-3 py-1 rounded-full ${theme===t?'bg-blue-600 text-white':'bg-slate-200'}`}>{t}</button>
        ))}
      </div>
      <input value={query} onChange={e=>setQuery(e.target.value)} placeholder="검색" className="mb-4 p-2 border rounded w-full max-w-md" />
      <div className="mb-4 flex gap-2">
        <button onClick={randomPick} className="bg-green-500 text-white px-4 py-2 rounded">랜덤 추천</button>
        <button onClick={()=>{setTheme('all');setQuery('')}} className="bg-slate-200 px-4 py-2 rounded">리셋</button>
      </div>

      <h2 className="font-semibold mb-2">추천 목록 ({filtered.length})</h2>
      <div className="grid md:grid-cols-2 gap-4">
        {filtered.map(p=>(
          <div key={p.id} className="bg-white rounded-lg shadow p-3">
            <img src={p.img} alt={p.name} className="h-32 w-full object-cover rounded" />
            <h3 className="mt-2 font-medium">{p.name}</h3>
            <p className="text-sm text-slate-600">{p.description}</p>
            <button onClick={()=>toggleFav(p.id)} className="mt-2 text-sm">{favorites.includes(p.id)?'★ 즐겨찾기':'☆ 즐겨찾기'}</button>
          </div>
        ))}
      </div>

      <h2 className="font-semibold mt-6 mb-2">즐겨찾기</h2>
      <ul className="list-disc ml-5 text-sm">
        {favorites.map(id => {
          const p=PLACES.find(x=>x.id===id)
          return <li key={id}>{p?.name}</li>
        })}
        {favorites.length===0 && <li className="text-slate-500">없음</li>}
      </ul>
    </div>
  )
}

// src/index.css
@tailwind base;
@tailwind components;
@tailwind utilities;

// postcss.config.cjs
module.exports = { plugins: { tailwindcss: {}, autoprefixer: {} } }

// tailwind.config.cjs
module.exports = { content: ['./index.html','./src/**/*.{js,jsx}'], theme:{extend:{}}, plugins:[] }

/* Run:
   npm install
   npm run dev
*/

