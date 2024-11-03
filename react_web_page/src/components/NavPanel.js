import { useNavigate, useLocation   } from "react-router-dom";


function NavPanel()
{
    const navigate = useNavigate();
    const location = useLocation();

    const navItems = [
        { path: "/intro", id: "intro-title-button", label: "Введение" },
        { path: "/description", id: "description-title-button", label: "Описание" },
        { path: "/posts", id: "posts-title-button", label: "Посты" },
        { path: "/conclusion", id: "conclusion-title-button", label: "Заключение" },
        { path: "/invert", id: "invert-title-button", label: "Демо" },
        { path: "/api", id: "api-title-button", label: "API" },
        { path: "/statistics", id: "statistics-title-button", label: "Статистика" }
    ];

    return (
        <div id="nav-panel-container">
            {navItems.map(item => (
                <button
                    key={item.id}
                    onClick={() => navigate(item.path)}
                    id={item.id}
                    className={location.pathname === item.path ? "active" : "inactive"}
                >
                    {item.label}
                </button>
            ))}
        </div>
    );
}

export default NavPanel;
