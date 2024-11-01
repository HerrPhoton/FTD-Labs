import { useState, useRef } from 'react';

function InvertImgPanel()
{
    const [resImage, setResImage] = useState(null);
    const [srcImage, setSrcImage] = useState(null);
    const fileInputRef = useRef(null);

    const handleSrcClick = () =>
    {
        fileInputRef.current.click();
    };

    const handleResClick = async () =>
    {
        await fetch('http://127.0.0.1:8080/invert_image/',
        {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ base64_image: srcImage }),
        })
        .then(response => response.json())
        .then(data => setResImage(data.inverted_image))
    };

    const handleFileChange = (event) =>
    {
        const file = event.target.files[0];

        if (file)
        {
            const reader = new FileReader();

            reader.onload = (e) =>
            {
                setSrcImage(e.target.result);
            };

            reader.readAsDataURL(file);
            setResImage(null);
        }

        else
            setSrcImage(null);
    };

    return (
        <div id="invert-img-content-container" className="page">

            <h1 className="title" id="main-title">Пересекающиеся части в аудиозаписях музыкальных произведений</h1>

            <div id="invert-img-container">

                <h2 id="invert-img-title">Инвертирование изображения</h2>

                <div id="images-container">

                    <div id="src-image-container" onClick={handleSrcClick}>

                        {srcImage ?
                        (
                            <img id="src-image" src={srcImage} alt="src" style={{ display: 'block' }} />
                        ) :
                        (
                            <span id="upload-text">Загрузить Изображение</span>
                        )}

                        <input type="file" id="src-image-input" accept="image/*" ref={fileInputRef} onChange={handleFileChange}/>

                    </div>

                    <div id="res-image-container" onClick={handleResClick}>

                        {resImage ?
                        (
                            <img id="res-image" src={resImage} alt="res" style={{ display: 'block' }} />
                        ) :
                        (
                            <span id="res-text">Инвертировать</span>
                        )}

                    </div>

                </div>

            </div>

        </div>
    );
}

export default InvertImgPanel;
