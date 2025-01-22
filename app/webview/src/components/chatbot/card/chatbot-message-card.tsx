import { Card, CardContent } from "@/components/ui/card";
import type { ChatbotMessage } from "@/domain/schema";
import { MessageRole } from "@/domain/value";

type Props = {
	value: ChatbotMessage;
};

export const ChatbotMessageCard = ({ value }: Props) => {
	return (
		<Card
			className={`flex flex-col gap-4 h-fit w-full ${value.role === MessageRole.USER ? "border-blue-800 bg-blue-500/25" : "bg-slate-500/25"}`}
		>
			<CardContent
				className={`overflow-auto flex flex-col h-full gap-4 px-4 py-2 text-sm font-semibold ${value.role === MessageRole.USER ? "" : ""}`}
			>
				<p className="whitespace-pre-wrap break-words">{value.content}</p>
			</CardContent>
		</Card>
	);
};
