import Link from "next/link";
import { Card } from "@/components/ui/card";
import type { Chatbot } from "@/domain/schema";

export const ChatbotCard = ({
	value,
}: {
	value: Chatbot;
}) => {
	return (
		<Card
			className={
				"relative flex flex-col gap-1.5 bg-gradient-to-b py-3.5 pl-3.5 pr-1.5 cursor-pointer overflow-hidden"
			}
		>
			<Link
				href={`/chatbot/${value.id}/message`}
				className={"absolute inset-0"}
			/>
			<div className={"flex flex-1 flex-col flex-start gap-1.5"}>
				<div className={"flex gap-1.5"}></div>
				<div
					className={
						"font-tiempos line-clamp-1 overflow-hidden text-base md:line-clamp-2 md:h-12 md:pr-2"
					}
				>
					{value.title}
				</div>
			</div>
		</Card>
	);
};
