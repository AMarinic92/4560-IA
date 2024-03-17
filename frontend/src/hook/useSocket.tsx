import { useEffect, useState } from "react";

import io, { Socket } from 'socket.io-client';

const useSocket = () => {
    const [socket, setSocket] = useState<Socket>();
    useEffect(
        () => {
            try {
                const socketConnection = io("http://localhost:5000");
                setSocket(socketConnection);
            } catch (error) {
                console.log("cant connect")
                // setSocket(null)
            }
            return () => {
                socket?.disconnect()
            }
        }
        , []
    )
    return socket as Socket;
}

export default useSocket;