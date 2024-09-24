import { useNavigate, useLocation   } from "react-router-dom";


function NavPanel() 
{
    const navigate = useNavigate();
    const location = useLocation();

    const is_active = (path) => location.pathname === path;

    return (
        <div id="nav-panel-container">

            <button onClick = {() => navigate("/")} id="intro-title-button" class={is_active("/") ? "active" : "inactive"}>Введение</button>
            <button onClick = {() => navigate("/description")} id="description-title-button" class={is_active("/description") ? "active" : "inactive"}>Описание</button>
            <button onClick = {() => navigate("/conclusion") } id="conclusion-title-button" class={is_active("/conclusion") ? "active" : "inactive"}>Заключение</button>

        </div>
    );
}

export default NavPanel;
