import { useEffect } from 'react';

export function usePageTracking(pageName) 
{
    useEffect(() => 
    {
        const startTime = Date.now();
        
        const handleBeforeUnload = () => 
            {
                const endTime = Date.now();
                const timeSpent = Math.round((endTime - startTime) / 1000);
                
                fetch(`http://localhost:8080/pages/${pageName}/kpi`, {
                    method: 'PUT',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({ time: timeSpent }),
                    keepalive: true
                });
            };

        window.addEventListener('beforeunload', handleBeforeUnload);

        return () => 
        {
            window.removeEventListener('beforeunload', handleBeforeUnload);
            
            const endTime = Date.now();
            const timeSpent = Math.round((endTime - startTime) / 1000);

            fetch(`http://localhost:8080/pages/${pageName}/kpi`, {
                method: 'PUT',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ time: timeSpent }),
            });
        };
    }, [pageName]);
}