import { useEffect, useState } from "react";
import { Problem } from "../interfaces/objects";

const Problems = ({problems}:{problems:Problem[]}) => {
    

    useEffect(
        ()=>{
            //setProblems([{ id: "1", type: "missing alt text", message: "image https://image.com/example.jpeg" }])
        }
        ,[]
    )

    return (
        <div tabIndex={0} className="collapse collapse-arrow border border-base-300 bg-primary mb-2">
            <input type="checkbox" />
            <div className="collapse-title text-xl font-medium">
                Problems
            </div>
            <div className="collapse-content">
                {
                    problems.map(
                        (problem: Problem) => {
                            return (
                                <div className="flex flex-row w-full justify-between  mb-2" key={problem.id}>
                                    <p className="font-bold capitalize">{problem.type}</p>
                                    <p>{problem.message}</p>
                                    <div className="divider" />
                                </div>
                            )
                        }
                    )
                }
            </div>
        </div>
    )
}

export default Problems;