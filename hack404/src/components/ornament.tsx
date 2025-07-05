import {
    faExclamationCircle,
    faArrowUpRightFromSquare,
  } from "@fortawesome/free-solid-svg-icons";
  import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
  import { useEffect, useState } from "react";
  

const Ornament = ({url}: {url: string}) => {
    const [loading, setLoading] = useState(true);
    const [links, setLinks] = useState<any[]>([]);
    const [error, setError] = useState<string | null>(null);

    useEffect(() => {
        console.log("url", url);

        setLoading(true);
        setError(null);
        
        if (url !== "") {
            fetch(`http://localhost:8000/scan-website/?url=${url}`)
                .then((res) => {
                    if (!res.ok) {
                        throw new Error(`HTTP error! status: ${res.status}`);
                    }
                    return res.json();
                })
                .then((data) => {
                    console.log("links", data);
                    try {
                        // Try to parse the response as JSON if it's a string
                        if (typeof data === 'string') {
                            const parsedData = JSON.parse(data);
                            setLinks(parsedData);
                        } else {
                            setLinks(data);
                        }
                    } catch (parseError) {
                        console.error("Failed to parse response:", parseError);
                        setError("Failed to parse response");
                    }
                })
                .catch((err) => {
                    console.error("Error fetching data:", err);
                    setError(err.message);
                })
                .finally(() => setLoading(false));
        } else {
            setLoading(false);
        }
    }, [url]);

    return (
        <div className="bg-white rounded-3xl shadow-md p-3 self-start sticky top-[160px] w-[130px] z-10 mr-2">
            <div className="flex flex-row rounded-3xl gap-3">
                <FontAwesomeIcon icon={faExclamationCircle} color="#B7E2DC" size="2x" />
                <h1
                className="text-[#22333B] text-2xl font-bold"
                style={{ fontFamily: "AlumniSans" }}
                >
                Support
                </h1>
            </div>
                <p
                    className="text-[#8A8A8A] text-sm mx-auto"
                    style={{ fontFamily: "AlumniSans" }}
                >
                    (see more info)
                </p>
                {loading ? (
                    <div className="border border-[#B7E2DC] p-2 rounded-xl flex flex-row justify-center">
                        <p className="text-[#8A8A8A] text-sm" style={{ fontFamily: "AlumniSans" }}>
                            Loading...
                        </p>
                    </div>
                ) : error ? (
                    <div className="border border-[#B7E2DC] p-2 rounded-xl flex flex-row justify-center">
                        <p className="text-red-500 text-sm" style={{ fontFamily: "AlumniSans" }}>
                            Error: {error}
                        </p>
                    </div>
                ) : links && links.length > 0 ? (
                    <div className="space-y-2">
                        {links.slice(0, 3).map((link, index) => (
                            <div key={index} className="border border-[#B7E2DC] p-2 rounded-xl flex flex-row justify-center">
                                <div className="w-[80%] flex flex-row justify-between my-auto">
                                    <h1
                                        className="text-[#8A8A8A] w-[90%] truncate pr-2 text-sm"
                                        style={{ fontFamily: "AlumniSans" }}
                                        title={link.name || link.url}
                                    >
                                        {link.name || link.url}
                                    </h1>
                                    <a
                                        href={link.url}
                                        target="_blank"
                                        rel="noopener noreferrer"
                                    >
                                        <FontAwesomeIcon
                                            className="mt-1 right-0"
                                            icon={faArrowUpRightFromSquare}
                                            color="#8A8A8A"
                                        />
                                    </a>
                                </div>
                            </div>
                        ))}
                    </div>
                ) : (
                    <div className="border border-[#B7E2DC] p-2 rounded-xl flex flex-row justify-center">
                        <p className="text-[#8A8A8A] text-sm" style={{ fontFamily: "AlumniSans" }}>
                            No supporting links found
                        </p>
                    </div>
                )}
            
        </div>
        
    )
}

export default Ornament 