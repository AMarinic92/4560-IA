import { useEffect, useState } from "react"
import { useAutoAnimate } from "@formkit/auto-animate/react"
import Header from "./components/header"
import Problems from "./components/problems"
import { Problem } from "./interfaces/objects";
import useSocket from "./hook/useSocket";
import { Socket } from "socket.io-client";


function App() {
  //const [socket, setSocket] = useState<Socket>();
  const [isReady, setIsReady] = useState<boolean>(false);
  const [problems, setProblems] = useState<Problem[]>([]);
  const socket = useSocket()

  const [loading, setLoading] = useState<boolean>(false);
  const [parent, enableAnimations] = useAutoAnimate();
  const [msgFailed, setMsgFailed] = useState<boolean>(false)


  const sendMessage = (url: string) => {
    try {
      console.log("sending msg")
      setLoading(true);
      socket?.emit("parse", { "website": url })
      // setProblems()
    } catch (error) {
      console.log(error)
      setMsgFailed(true)
    }
  }

  const messageEvent = (data: any) => {
    // set problems
    setProblems(data.response)
    //tell frontend components we are ready
    setLoading(false);
    setIsReady(true);
  }


  useEffect(
    () => {
      try {
        console.log(socket)
        socket?.on("reply", (data: any) => {
          enableAnimations(true)
          console.log(`reply ${data?.response}`);
          messageEvent(data)
        })
        
        //disconnect
        socket.on("disconnect",(reason:Socket.DisconnectReason)=>{
          console.log(reason)
        })

      } catch (error) {
        console.log("cant connect")
      }

    }, [socket, problems]
  )

  return (
    <div ref={parent} className="container h-96 w-full  px-5 py-5">
      {socket ? (<Header
        changeIsReady={

          async (val: boolean, url: string) => {
            sendMessage(url)
            console.log(val)
          }
        }
      />) : ""}

      {msgFailed ? "message failed to send" : ""}

      {
        loading && (
          <div className="flex flex-col justify-center ">
            <span className="loading loading-bars loading-lg"></span>
          </div>
        )
      }

      {
        isReady ? (<div className="flex flex-col mt-5 ">

          <Problems problems={problems} />

        </div>
        ) : ""
      }


    </div>
  )
}

export default App
