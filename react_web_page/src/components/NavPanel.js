import { useNavigate, useLocation   } from "react-router-dom";


function NavPanel()
{
    const navigate = useNavigate();
    const location = useLocation();

    const is_active = (path) => location.pathname === path;
    const set_class = (path) => is_active(path) ? "active" : "inactive";

    const root_path = "/";
    const description_path = "/description";
    const posts_path = "/posts";
    const conclusion_path = "/conclusion";
    const invert_path = "/invert";
    const api_path = "/api";

    return (
        <div id="nav-panel-container">

            <button onClick = {() => navigate(root_path)} id="intro-title-button" className={set_class(root_path)}>Введение</button>
            <button onClick = {() => navigate(description_path)} id="description-title-button" className={set_class(description_path)}>Описание</button>
            <button onClick = {() => navigate(posts_path)} id="intro-title-button" className={set_class(posts_path)}>Посты</button>
            <button onClick = {() => navigate(conclusion_path) } id="conclusion-title-button" className={set_class(conclusion_path)}>Заключение</button>
            <button onClick = {() => navigate(invert_path) } id="invert-title-button" className={set_class(invert_path)}>Демо</button>
            <button onClick = {() => navigate(api_path) } id="api-title-button" className={set_class(api_path)}>API</button>

        </div>
    );
}

export default NavPanel;
