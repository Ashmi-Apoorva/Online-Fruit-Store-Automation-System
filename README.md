# Online Fruit Store Automation System
A Python-based system that automates the catalog update process for an online fruit store, integrating new products provided by suppliers into the online store. The system processes images and descriptions for each new fruit item, uploads the information to the store's catalog, and sends a report back to the suppliers via email. It also continuously monitors the server's health to ensure uptime and reliable operation.
    <h2>Key Functionalities</h2>
    <ul>
        <li><strong>Image and Description Processing</strong>
            <ul>
                <li>Converts high-resolution <code>.TIF</code> images to optimized <code>.jpeg</code> format.</li>
                <li>Extracts fruit name, description, and weight from <code>.txt</code> files.</li>
                <li>Generates HTML files with product image and description for catalog updates.</li>
            </ul>
        </li>
        <li><strong>Data Upload and Integration</strong>
            <ul>
                <li>Uploads images to an image endpoint and descriptions to a catalog endpoint on a Django server.</li>
            </ul>
        </li>
        <li><strong>Supplier Notification</strong>
            <ul>
                <li>Creates a PDF report with fruit names and weights, then emails it to the supplier.</li>
            </ul>
        </li>
        <li><strong>System Health Monitoring</strong>
            <ul>
                <li>Monitors server health and sends alert emails if the system becomes unhealthy, i.e., if CPU usage is over 80%, available disk space is lower than 20%, available memory is less than 100MB or if the hostname "localhost" cannot be resolved to "127.0.0.1"</li>
            </ul>
        </li>
    </ul>
 
    


   
