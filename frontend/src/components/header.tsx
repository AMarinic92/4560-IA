import { useState } from "react";
import { getUrl } from "../utils/chrome";
import { ChangeIsReady } from "../interfaces/functions";
import { checker } from "../utils/checker"


const Header = ({ changeIsReady }: { changeIsReady: ChangeIsReady }) => {
    const [init, setInit] = useState<boolean>(false)
    const [website, setWebsite] = useState<string | null>(null)


    return (
        <div className="flex flex-col">
            <h1 className="mb-3 text-xl font-bold">Accessability Checker</h1>

            <div className="flex flex-row mb-1 w-1/2 ">
                <p>Checking</p>
                <p className="font-bold text-ellipsis ">{website}</p>
            </div>
            <div className="flex flex-row  justify-between">

                <button
                    className="btn btn-secondary "
                    onClick={
                        async () => {
                            const url = await getUrl();
                            if (url) {
                                checker(url)
                                setWebsite(url);
                                changeIsReady(true, url as string);
                                setInit(true);
                            }

                        }
                    }
                    disabled={init}
                >
                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={1.5} stroke="currentColor" className="w-6 h-6">
                        <path strokeLinecap="round" strokeLinejoin="round" d="m15.75 15.75-2.489-2.489m0 0a3.375 3.375 0 1 0-4.773-4.773 3.375 3.375 0 0 0 4.774 4.774ZM21 12a9 9 0 1 1-18 0 9 9 0 0 1 18 0Z" />
                    </svg>

                    Analyze website
                </button>
                <button
                    className="btn btn-info"
                    onClick={
                        ()=>{
                            const modal = document?.getElementById('info_modal') as HTMLDialogElement;
                            modal?.showModal();
                        }
                    }
                >
                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={1.5} stroke="currentColor" className="w-6 h-6">
                        <path strokeLinecap="round" strokeLinejoin="round" d="m11.25 11.25.041-.02a.75.75 0 0 1 1.063.852l-.708 2.836a.75.75 0 0 0 1.063.853l.041-.021M21 12a9 9 0 1 1-18 0 9 9 0 0 1 18 0Zm-9-3.75h.008v.008H12V8.25Z" />
                    </svg>

                    what is this?
                </button>
            </div>

        </div>
    )
}

export default Header;