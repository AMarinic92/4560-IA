import { useState } from "react";
import { getUrl } from "../utils/chrome";

function Stats() {
    return (
        <div className="flex flex-row justify-between">

            <div className="">
                <div>Score</div>
                <div className="flex justify-center items-center bg-primary rounded-full w-12 h-12  ">
                    <p className="font-bold">8.5</p>
                </div>
            </div>
            <div>
                <div className="mb-1"> Score list</div>

                <p className="font-bold">Readability - 8.5</p>
                <p className="font-bold">Alt Text - 8.5</p>



            </div>

        </div>

    )
}

const Header = ({changeIsReady}:any) => {
    const [init, setInit] = useState<boolean>(false)
    return (
        <div className="flex flex-col">
            <h1 className="mb-3 text-xl font-bold">Accessability Checker</h1>
           
            {!init ? ( <button
                className="btn btn-secondary mt-5"
                onClick={
                    async ()=>{
                        const url = await getUrl()
                        setInit(true);
                        changeIsReady(true)
                    }
                }
            >
                Analyze website
            </button>): (<Stats />)}

        </div>
    )
}

export default Header;