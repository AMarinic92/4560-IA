import { useEffect, useState } from "react"
import Header from "./components/header"
import Problems from "./components/problems"
import Suggestions from "./components/suggestions"
import { Problem } from "./interfaces/objects";


function App() {

  const [isReady, setIsReady] = useState<boolean>(false);
  const [problems, setProblems] = useState<Problem[]>([]);

  const getProblems = async () => {
    const response = await fetch("http://localhost:8080/api/parse");

    if (response.ok) {
      const results = await response.json();
      return results.problems;
    }

    return null;

  }

  useEffect(
    () => {


    }, [problems]
  )

  return (
    <div className="container h-96 w-full  px-5 py-5">
      <Header
        changeIsReady={
          (val: boolean) => {
            setIsReady(val)
          }
        }
      />

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
