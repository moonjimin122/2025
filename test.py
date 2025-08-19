/*
Updated React + Vite + Tailwind Korean Movie Theme Recommender
Now includes 20 Korean movies (5 for each theme: romance, action, documentary, comedy)
*/

// package.json
{
  "name": "movie-theme-recommender",
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
    <title>Korean Movie Recommender</title>
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
export const MOVIES = [
  // Romance
  { id:1, title:"건축학개론", theme:"romance", description:"첫사랑을 다시 마주한 청춘 멜로", img:"https://upload.wikimedia.org/wikipedia/ko/6/64/Architecture_101.jpg" },
  { id:2, title:"클래식", theme:"romance", description:"세대를 아우르는 사랑 이야기", img:"https://upload.wikimedia.org/wikipedia/ko/3/3e/The_Classic_film_poster.jpg" },
  { id:3, title:"너의 결혼식", theme:"romance", description:"첫사랑과의 10년 인연", img:"https://upload.wikimedia.org/wikipedia/ko/5/55/On_Your_Wedding_Day.jpg" },
  { id:4, title:"더 테이블", theme:"romance", description:"카페 테이블에서 오가는 네 가지 이야기", img:"https://upload.wikimedia.org/wikipedia/ko/7/75/The_Table_film.jpg" },
  { id:5, title:"조제", theme:"romance", description:"운명처럼 다가온 사랑", img:"https://upload.wikimedia.org/wikipedia/ko/f/fd/Jos%C3%A9e_2020.jpg" },

  // Action
  { id:6, title:"아저씨", theme:"action", description:"과거를 숨긴 남자의 구출 액션", img:"https://upload.wikimedia.org/wikipedia/ko/7/75/The_Man_From_Nowhere.jpg" },
  { id:7, title:"부산행", theme:"action", description:"좀비로부터의 생존 열차", img:"https://upload.wikimedia.org/wikipedia/ko/9/95/Train_to_Busan.jpg" },
  { id:8, title:"베테랑", theme:"action", description:"강력반 형사의 통쾌한 수사극", img:"https://upload.wikimedia.org/wikipedia/ko/f/f0/Veteran_%28film%29.jpg" },
  { id:9, title:"범죄도시", theme:"action", description:"강력반 형사와 범죄조직의 대결", img:"https://upload.wikimedia.org/wikipedia/ko/d/d1/The_Outlaws.jpg" },
  { id:10, title:"신세계", theme:"action", description:"언더커버 형사의 조직 잠입", img:"https://upload.wikimedia.org/wikipedia/ko/c/cf/New_World_film_poster.jpg" },

  // Documentary
  { id:11, title:"님아, 그 강을 건너지 마오", theme:"documentary", description:"노부부의 사랑과 삶", img:"https://upload.wikimedia.org/wikipedia/ko/5/5b/My_Love%2C_Don%27t_Cross_That_River.jpg" },
  { id:12, title:"워낭소리", theme:"documentary", description:"노부부와 소의 정겨운 삶", img:"https://upload.wikimedia.org/wikipedia/ko/4/41/Old_Partner.jpg" },
  { id:13, title:"김군", theme:"documentary", description:"1980년 광주의 기억", img:"https://upload.wikimedia.org/wikipedia/ko/d/dc/Kim-Gun-poster.jpg" },
  { id:14, title:"또 다른 가족", theme:"documentary", description:"삼성 백혈병 피해자 가족 이야기", img:"https://upload.wikimedia.org/wikipedia/ko/f/f1/Another_Family.jpg" },
  { id:15, title:"북극의 눈물", theme:"documentary", description:"북극의 환경 다큐멘터리", img:"https://via.placeholder.com/300x450.png?text=%EB%B6%81%EA%B7%B9%EC%9D%98+%EB%88%88%EB%AC%BC" },

  // Comedy
  { id:16, title:"극한직업", theme:"comedy", description:"치킨 장사로 위장한 마약 수사반", img:"https://upload.wikimedia.org/wikipedia/ko/7/76/Extreme_Job.jpg" },
  { id:17, title:"수상한 그녀", theme:"comedy", description:"청춘으로 돌아간 할머니의 이야기", img:"https://upload.wikimedia.org/wikipedia/ko/d/de/Miss_Granny.jpg" },
  { id:18, title:"해적: 바다로 간 산적", theme:"comedy", description:"해적과 산적의 유쾌한 모험", img:"https://upload.wikimedia.org/wikipedia/ko/0/0f/The_Pirates_poster.jpg" },
  { id:19, title:"스물", theme:"comedy", description:"스무 살 청춘들의 성장담", img:"https://upload.wikimedia.org/wikipedia/ko/0/0a/Twenty_film_poster.jpg" },
  { id:20, title:"타짜", theme:"comedy", description:"화투판의 세계와 인간 욕망", img:"https://upload.wikimedia.org/wikipedia/ko/e/eb/Tazza-The_High_Rollers.jpg" }
]

// src/App.jsx
import React, { useState, useMemo, useEffect } from 'react'
import { MOVIES } from './data'

const THEMES = ['all','romance','action','documentary','comedy']

export default function App() {
  const [theme, setTheme] = useState('all')
  const [query, setQuery] = useState('')
  const [favorites, setFavorites] = useState(() => {
    try { return JSON.parse(localStorage.getItem('fav_movies')||'[]') } catch { return [] }
  })

  useEffect(()=>{ localStorage.setItem('fav_movies', JSON.stringify(favorites)) },[favorites])

  const filtered = useMemo(()=>{
    return MOVIES.filter(m => (theme==='all'||m.theme===theme) && (m.title.toLowerCase().includes(query.toLowerCase())||m.description.toLowerCase().includes(query.toLowerCase())))
  },[theme,query])

  const toggleFav = (id)=> setFavorites(prev => prev.includes(id)? prev.filter(x=>x!==id) : [...prev,id])

  const randomPick = ()=>{
    if(filtered.length===0) return alert("조건에 맞는 영화가 없습니다.")
    const m = filtered[Math.floor(Math.random()*filtered.length)]
    alert(`${m.title}: ${m.description}`)
  }

  return (
    <div className="min-h-screen bg-slate-50 p-6">
      <h1 className="text-2xl font-bold mb-4">한국 영화 추천</h1>
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

      <h2 className="font-semibold mb-2">추천 영화 목록 ({filtered.length})</h2>
      <div className="grid md:grid-cols-2 gap-4">
        {filtered.map(m=>(
          <div key={m.id} className="bg-white rounded-lg shadow p-3">
            <img src={m.img} alt={m.title} className="h-40 w-full object-cover rounded" />
            <h3 className="mt-2 font-medium">{m.title}</h3>
            <p className="text-sm text-slate-600">{m.description}</p>
            <button onClick={()=>toggleFav(m.id)} className="mt-2 text-sm">{favorites.includes(m.id)?'★ 즐겨찾기':'☆ 즐겨찾기'}</button>
          </div>
        ))}
      </div>

      <h2 className="font-semibold mt-6 mb-2">즐겨찾기</h2>
      <ul className="list-disc ml-5 text-sm">
        {favorites.map(id => {
          const m=MOVIES.find(x=>x.id===id)
          return <li key={id}>{m?.title}</li>
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
