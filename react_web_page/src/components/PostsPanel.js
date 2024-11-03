import { useEffect, useState } from 'react';

function PostsPanel()
{
    const [posts, setPosts] = useState([]);
    const [visiblePostCnt, setVisiblePostCnt] = useState(3);

    const fetchPosts = async () =>
    {
        await fetch('http://127.0.0.1:8080/posts/')
        .then(response => response.json())
        .then(data => setPosts(data.data.posts))
    };

    useEffect(() =>
    {
        fetchPosts();
    }, []);

    return (
        <div id="posts-content-container" className="page">

            <h1 className="title" id="main-title">Пересекающиеся части в аудиозаписях музыкальных произведений</h1>

            <div id="posts-container">

                <h2 id="posts-title">Посты</h2>

                <div id="slider-container">

                    <h3 className="title">Количество постов: {visiblePostCnt}</h3>
                    <input type="range" min="1" max="20" value={visiblePostCnt} className="slider" onChange={(event) => setVisiblePostCnt(event.target.value)}></input>

                </div>

                <div id="posts-list">
                {
                    posts.slice(0, visiblePostCnt).map(post => (

                        <div id="post">

                            <h3>{post.title}</h3>
                            <p>{post.body}</p>

                        </div>
                ))}
                </div>

            </div>


        </div>
    );
}

export default PostsPanel;
