import React, { useState } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [imageSrc, setImageSrc] = useState('');
  const [promptValue, setPromptValue] = useState('');

  const handlePromptSubmit = async () => {
    try {
      // Замените URL на ваш URL сервера FastAPI
      const response = await axios.post('http://127.0.0.1:3333/prompt', {
        prompt: promptValue,
      });

      // Обработка ответа от сервера
      console.log('Ответ от сервера:', response.data);

      // Обновление состояния изображения
      setImageSrc(`data:image/png;base64,${response.data.image}`);
    } catch (error) {
      console.error('Ошибка при отправке промпта на сервер:', error);
    }
  };

  return (
    <div className="App">
      <div className="prompt-container">
        <input
          type="text"
          placeholder="Введите промпт"
          value={promptValue}
          onChange={(e) => setPromptValue(e.target.value)}
        />
        <button onClick={handlePromptSubmit}>Отправить</button>
      </div>
      <div className="image-container">
        {imageSrc && <img src={imageSrc} alt="Изображение" />}
      </div>
    </div>
  );
}

export default App;
