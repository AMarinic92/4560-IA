import { useEffect, useState } from "react"
import { useAutoAnimate } from "@formkit/auto-animate/react"
import Header from "./components/header"
import Problems from "./components/problems"
import { Problem } from "./interfaces/objects";
import useSocket from "./hook/useSocket";
import { Socket } from "socket.io-client";
import InfoModal from "./components/info_modal";
import LoadingCollapse from "./components/loading_collapse";


function App() {
  //const [socket, setSocket] = useState<Socket>();
  const [isReady, setIsReady] = useState<boolean>(false);
  const [problems, setProblems] = useState<Problem[]>([]);
  const socket = useSocket()

  const [loading, setLoading] = useState<boolean>(false);
  const [parent, enableAnimations] = useAutoAnimate();
  const [msgFailed, setMsgFailed] = useState<boolean>(false)

  const resetState = () => {
    setProblems([]);
    setLoading(false);
  }


  const sendMessage = (url: string) => {
    try {
      console.log("sending msg");
      setLoading(true);
      socket?.emit("parse", { "website": url });
      // setProblems()
    } catch (error) {
      console.log(error);
      setMsgFailed(true);
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
        socket.on("disconnect", (reason: Socket.DisconnectReason) => {
          console.log(reason)
        })

      } catch (error) {
        console.log("cant connect")
      }

    }, [socket, problems]
  )

  return (
    <div ref={parent} className=" ">
      {socket ? (
        <Header

          resetState={resetState}
          changeIsReady={

            async (val: boolean, url: string) => {
              sendMessage(url)
              console.log(val)
            }
          }
        />
      ) : ""}

      {msgFailed ? "message failed to send" : ""}

      {
        loading && (
          <div className="px-2 mt-5">
            <LoadingCollapse />
          </div>
        )
      }

      {
        isReady ? (
          <div className="px-2 mt-5">

            <Problems problems={problems} />

          </div>
        ) : ""
      }

      <InfoModal />
    </div>
  )
}

export default App
