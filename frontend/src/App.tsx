import { useEffect, useState } from "react"
import io, { Socket } from 'socket.io-client';
import { useAutoAnimate } from "@formkit/auto-animate/react"
import Header from "./components/header"
import Problems from "./components/problems"
import Suggestions from "./components/suggestions"
import { Problem } from "./interfaces/objects";
import useSocket from "./hook/useSocket";


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
      socket?.emit("parse", { "website": url })
    } catch (error) {
      console.log(error)
      setMsgFailed(true)

    }

  }

  

  useEffect(
    () => {
      try {
       console.log(socket)
        socket?.on("reply", (data: any) => {
         // alert("reply")
          console.log(`reply ${data.response}`)
          //socket.disconnect()
        })

      } catch (error) {
        console.log("cant connect")
       // setSocket(null)
      }
     
    }, [socket ,problems]
  )

  return (
    <div ref={parent} className="container h-96 w-full  px-5 py-5">
      {socket ? (<Header
        changeIsReady={

          async (val: boolean, url: string) => {
            alert(url)
            sendMessage(url)
            // await getProblems(url)
            setIsReady(val);

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
          <Suggestions />



        </div>
        ) : ""
      }


    </div>
  )
}

export default App
