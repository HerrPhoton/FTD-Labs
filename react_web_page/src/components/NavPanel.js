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

    return (
        <div id="nav-panel-container">

            <button onClick = {() => navigate(root_path)} id="intro-title-button" class={set_class(root_path)}>Введение</button>
            <button onClick = {() => navigate(description_path)} id="description-title-button" class={set_class(description_path)}>Описание</button>
            <button onClick = {() => navigate(posts_path)} id="intro-title-button" class={set_class(posts_path)}>Посты</button>
            <button onClick = {() => navigate(conclusion_path) } id="conclusion-title-button" class={set_class(conclusion_path)}>Заключение</button>

        </div>
    );
}

export default NavPanel;
