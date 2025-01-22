import Link from "next/link";
import { Card } from "@/components/ui/card";
import { MessagesSquare } from "lucide-react";
import type { Chatbot } from "@/domain/schema";
import { EditChatbotDialog } from "@/components/chatbot/dialog/edit-chatbot-dialog";
import { DeleteChatbotDialog } from "@/components/chatbot/dialog/delete-chatbot-dialog";

export const ChatbotCard = ({
	value,
}: {
	value: Chatbot;
}) => {
	return (
		<Card
			className={
				"relative w-full h-36 flex flex-col gap-1.5 py-3.5 pl-3.5 pr-1.5 cursor-pointer overflow-hidden border-blue-800"
			}
		>
			<Link
				href={`/chatbot/${value.id}/message`}
				className={"absolute inset-0 bg-blue-500/25 hover:bg-blue-700/25"}
			/>
			<div className={"flex flex-1 flex-col flex-start gap-1.5"}>
				<div className={"flex gap-1.5"}>
					<MessagesSquare />
				</div>
				<div
					className={
						"font-tiempos line-clamp-1 overflow-hidden text-base md:line-clamp-2 md:h-12 md:pr-2"
					}
				>
					{value.title}
				</div>
			</div>
			<div className={"absolute z-20 right-2 bottom-2 flex"}>
				<EditChatbotDialog value={value} />
				<DeleteChatbotDialog value={value} />
			</div>
		</Card>
	);
};
