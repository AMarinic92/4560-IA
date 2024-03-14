import { useEffect, useState } from "react"
import io, { Socket } from 'socket.io-client';
import { useAutoAnimate } from "@formkit/auto-animate/react"
import Header from "./components/header"
import Problems from "./components/problems"
import Suggestions from "./components/suggestions"
import { Problem } from "./interfaces/objects";


function App() {
  const [socket, setSocket] = useState<Socket | null>(null)
  const [isReady, setIsReady] = useState<boolean>(false);
  const [problems, setProblems] = useState<Problem[]>([]);

  const [loading, setLoading] = useState<boolean>(false);
  const [parent, enableAnimations] = useAutoAnimate();
  const [msgFailed , setMsgFailed]= useState<boolean>(false)


  const sendMessage =(url:string)=>{
    try{
      socket?.emit("parse",{"website":url})
    }catch(error){
      console.log(error)
      setMsgFailed(true)

    }
    
  }

  // const getProblems = async (url: string) => {
  //   setLoading(true);
  //   const response = await fetch("http://localhost:8080/api/parse", {
  //     method: "POST",
  //     body: JSON.stringify({
  //       "website": url

  //     })
  //   });

  //   if (response.ok) {
  //     const results = await response.json();

  //     setProblems(results.problems);
  //     // return results.problems;
  //   } else {
  //     throw new Error("oops");
  //   }
  //   setLoading(false);


  // }

  useEffect(
    () => {
      try {


        const socketConnection = io("http://localhost:5001");
        if (socketConnection) {
          setSocket(socketConnection);
        } else {
          console.log("socket is not active");
          alert("socket is not on")
        }
      } catch (error) {
        console.log("cant connect")
        setSocket(null)
      }
      return () => {
        socket?.disconnect()
      }

    }, [problems]
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

      {msgFailed?"message failed to send":""}

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
