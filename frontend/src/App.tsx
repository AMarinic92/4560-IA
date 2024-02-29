import { useEffect, useState } from "react"
import { useAutoAnimate } from "@formkit/auto-animate/react"
import Header from "./components/header"
import Problems from "./components/problems"
import Suggestions from "./components/suggestions"
import { Problem } from "./interfaces/objects";


function App() {

  const [isReady, setIsReady] = useState<boolean>(false);
  const [problems, setProblems] = useState<Problem[]>([]);
  const [loading, setLoading] = useState<boolean>(false);
  const [parent, enableAnimations] = useAutoAnimate();

  const getProblems = async (url: string) => {
    setLoading(true);
    const response = await fetch("http://localhost:8080/api/parse", {
      method: "POST",
      body: JSON.stringify({
        "website": url
      })
    });

    if (response.ok) {
      const results = await response.json();
      setProblems(results.problems);
      // return results.problems;
    } else {
      throw new Error("oops");
    }
    setLoading(false);


  }

  useEffect(
    () => {


    }, [problems]
  )

  return (
    <div ref={parent} className="container h-96 w-full  px-5 py-5">
      <Header
        changeIsReady={
          async (val: boolean, url: string) => {

            await getProblems(url)
            setIsReady(val);
          }
        }
      />
      
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
